def prepare_order_info(order):
    """Prepares the customer information for the receipt"""
    return "Customer ID : {}<br>" \
           "Order ID : {}<br>" \
           "Date   : {}<br>".format(order.customer_id, order.order_id, order.order_date)


def prepare_items_info(order):
    """Prepare the receipt items"""
    items_info = ""
    for item in order.items:
        item_info = '<tr class="service">' \
                    '<td class="tableitem"><p class="itemtext">{}</p></td>' \
                    '<td class="tableitem"><p class="itemtext">{}</p></td>' \
                    '<td class="tableitem"><p class="itemtext">{}</p></td>' \
                    '</tr>'.format(item['name'], item['quantity'], item['amount'])
        items_info += item_info
    return items_info


def prepare_receipt_email(order):
    """Prepares the full receipt contents"""
    order_info = prepare_order_info(order)
    items_info = prepare_items_info(order)

    file = open('mailer/receipt_template.txt', mode='r')
    template = str(file.read())
    file.close()

    return template % (order_info, items_info, order.amount)
